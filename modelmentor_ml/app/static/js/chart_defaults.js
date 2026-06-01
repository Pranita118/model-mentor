// ── Set Chart.js 4 global defaults so all charts inherit theme-aware colors ──
(function setChartDefaults() {
  const isDark = (document.documentElement.getAttribute('data-theme') || 'dark') !== 'light';
  const tickColor  = isDark ? '#c8cfe0' : '#1a2030';
  const gridColor  = isDark ? 'rgba(100,110,140,0.25)' : 'rgba(0,0,0,0.08)';
  Chart.defaults.color                        = tickColor;
  Chart.defaults.borderColor                  = gridColor;
  if (Chart.defaults.scale) {
    Chart.defaults.scale.ticks = Chart.defaults.scale.ticks || {};
    Chart.defaults.scale.ticks.color          = tickColor;
    Chart.defaults.scale.grid = Chart.defaults.scale.grid || {};
    Chart.defaults.scale.grid.color           = gridColor;
  }
  Chart.defaults.plugins.legend.labels.color  = tickColor;
  Chart.defaults.plugins.tooltip.backgroundColor = isDark ? '#1a1c26' : '#ffffff';
  Chart.defaults.plugins.tooltip.titleColor   = isDark ? '#e8eaf2' : '#0d1117';
  Chart.defaults.plugins.tooltip.bodyColor    = isDark ? '#8b90a8' : '#3a4050';
  Chart.defaults.plugins.tooltip.borderColor  = isDark ? '#272a38' : '#d5dbe8';
  Chart.defaults.plugins.tooltip.borderWidth  = 1;
})();
