// Stacks — number/format helpers.
// Reconstructed: every view imports this and uses `formatLib.formatNumber`.

/**
 * Format a number with Indian-style digit grouping (lakh/crore), used for
 * the Rs amounts shown across budgets, expenses and dashboards.
 * Falls back gracefully for null / undefined / non-numeric input.
 *
 * @param {number|string|null} value
 * @param {number} [decimals=2] maximum fraction digits
 * @returns {string}
 */
function formatNumber(value, decimals = 2) {
  if (value === null || value === undefined || value === "") return "0";
  const num = typeof value === "number" ? value : Number(value);
  if (Number.isNaN(num)) return "0";

  return new Intl.NumberFormat("en-IN", {
    minimumFractionDigits: 0,
    maximumFractionDigits: decimals,
  }).format(num);
}

/**
 * Convenience helper for an Rs-prefixed amount.
 * @param {number|string|null} value
 * @returns {string}
 */
function formatCurrency(value) {
  return `Rs ${formatNumber(value)}`;
}

export default {
  formatNumber,
  formatCurrency,
};

export { formatNumber, formatCurrency };
