// core types for polyphony handler

export type SourceID = string;
export type EpistemicTag = string;
export type Hash = string;

export interface FieldState {
  source_id: SourceID;
  timestamp: string; // ISO8601
  epistemic_tag: EpistemicTag;
  content: string;
  content_hash: Hash;
}

export interface PolyphonicView {
  fields: ReadonlyArray<FieldState>;
}

export interface EpistemicTraceRow {
  source_id: SourceID;
  content_hash: Hash;
  references?: string[];
}

export interface EpistemicTraceTable {
  rows: ReadonlyArray<EpistemicTraceRow>;
}

export interface TensionEdge {
  from: SourceID;
  to: SourceID;
  score: number; // [0..1]
}

export interface TensionMap {
  edges: ReadonlyArray<TensionEdge>;
}
