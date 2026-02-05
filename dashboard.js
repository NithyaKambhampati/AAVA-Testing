async function loadDashboard() {
  try {
    const widgets = await Promise.allSettled(fetchWidgets());
    renderWidgets(widgets);
  } catch (error) {
    console.error("Dashboard load failed", error);
  }
}
