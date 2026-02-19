import axios from "axios";

const API = axios.create({
  baseURL: import.meta.env.VITE_API_BASE,
});


export const getIncidents = async () => {
  const res = await API.get("/events");
  return res.data;
};
