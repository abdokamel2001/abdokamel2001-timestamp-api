export default function handler(req, res) {
  const { timestamp } = req.query;

  if (!timestamp) {
    return res.status(400).json({ error: "Missing timestamp" });
  }

  const unix = parseInt(timestamp, 10);
  if (isNaN(unix)) {
    return res.status(400).json({ error: "Invalid timestamp" });
  }

  const date = new Date(unix * 1000);
  const readable = date.toISOString().replace("T", " ").replace("Z", "");

  return res.status(200).json({ unix, readable });
}
