export type AIAnalysis = {
  root_cause: string;
  confidence: string;
};

export type Incident = {
  id: number;
  title: string;
  description: string;
  status_id: number;
  priority_id: number;
  created_at: string;
  ai_analysis: AIAnalysis;
};

export type IncidentState = {
  data: Incident[];
  loading: boolean;
  error: string | null;
};
