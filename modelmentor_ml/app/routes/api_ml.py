"""Optional REST surface for Python/ML utilities (UI remains client-driven)."""
from flask import Blueprint, jsonify, request

from app.ml.tabular import describe_dataframe, iqr_outlier_mask

bp = Blueprint("api_ml", __name__, url_prefix="/api/ml")


@bp.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "modelmentor-ml"})


@bp.route("/describe", methods=["POST"])
def describe():
    """
    Accepts JSON: { "records": [ { "col": v, ... }, ... ] }
    Returns pandas-like summary consumable by notebooks or future UI hooks.
    """
    payload = request.get_json(silent=True) or {}
    records = payload.get("records")
    if not isinstance(records, list) or not records:
        return jsonify({"error": "records must be a non-empty list of objects"}), 400
    summary = describe_dataframe(records)
    return jsonify(summary)


@bp.route("/outliers-iqr", methods=["POST"])
def outliers_iqr():
    payload = request.get_json(silent=True) or {}
    records = payload.get("records")
    column = payload.get("column")
    if not isinstance(records, list) or not records or not column:
        return jsonify({"error": "records (list) and column (string) required"}), 400
    try:
        mask = iqr_outlier_mask(records, column)
    except KeyError:
        return jsonify({"error": "unknown column"}), 400
    return jsonify({"column": column, "outlier_row_indices": [i for i, x in enumerate(mask) if x]})
