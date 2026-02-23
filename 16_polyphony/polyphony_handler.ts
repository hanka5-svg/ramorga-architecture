import {
  FieldState,
  PolyphonicView,
  EpistemicTraceTable,
  TensionMap
} from "./polyphony_types";

export interface PolyphonyHandler {
  ingest(input: ReadonlyArray<FieldState>): {
    view: PolyphonicView;
    trace: EpistemicTraceTable;
    tension?: TensionMap;
  };
}
