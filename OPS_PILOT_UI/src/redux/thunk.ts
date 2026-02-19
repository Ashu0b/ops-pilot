import { createAsyncThunk } from "@reduxjs/toolkit";
import { getIncidents } from "../services/incidentApi";

export const fetchIncidents = createAsyncThunk(
  "incidents/fetchIncidents",
  async (_, thunkAPI) => {
    try {
      return await getIncidents();
    } catch (err: any) {
      return thunkAPI.rejectWithValue(err.message);
    }
  },
);
