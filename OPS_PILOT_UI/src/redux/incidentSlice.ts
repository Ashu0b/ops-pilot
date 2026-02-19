import { createSlice } from "@reduxjs/toolkit";
import { fetchIncidents } from "./thunk";
import type { IncidentState } from "../types/types";

const initialState: IncidentState = {
  data: [],
  loading: false,
  error: null,
};

const incidentsSlice = createSlice({
  name: "incidents",
  initialState,
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchIncidents.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchIncidents.fulfilled, (state, action) => {
        state.loading = false;
        state.data = action.payload;
      })
      .addCase(fetchIncidents.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  },
});

export default incidentsSlice.reducer;
