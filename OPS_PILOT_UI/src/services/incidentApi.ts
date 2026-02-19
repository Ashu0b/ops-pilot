import axios from "axios";

const API = axios.create({
  baseURL: "/api",
});

export const getIncidents = async () => {
  const res = await API.get("/events");
  return res.data;
};
