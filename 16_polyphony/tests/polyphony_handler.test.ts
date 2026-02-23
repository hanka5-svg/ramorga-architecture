import { PolyphonyHandler } from "../polyphony_handler";
import fixture from "../fixtures/case_3_sources.yaml";

test("no content modification", () => {
  const handler: PolyphonyHandler = /* stub */;
  const out = handler.ingest(fixture);
  expect(out.view.fields.map(f => f.content)).toEqual(
    fixture.map(f => f.content)
  );
});

test("source attribution preserved", () => {
  const handler: PolyphonyHandler = /* stub */;
  const out = handler.ingest(fixture);
  expect(out.trace.rows.length).toBe(fixture.length);
});

test("no epistemic closure", () => {
  const handler: PolyphonyHandler = /* stub */;
  const out = handler.ingest(fixture);
  expect(out.tension).toBeDefined(); // optional, read-only
});
