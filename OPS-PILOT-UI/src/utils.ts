import { EventStatusEnum, PriorityEnum } from "./enum";

const formatEnumLabel = (value: string) =>
  value
    .toLowerCase()
    .replace(/_/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());

export const getStatusLabel = (statusId?: number) => {
  const entry = Object.entries(EventStatusEnum).find(([, v]) => v === statusId);
  return entry ? formatEnumLabel(entry[0]) : "Unknown";
};

export const getPriorityLabel = (priorityId?: number) => {
  const entry = Object.entries(PriorityEnum).find(([, v]) => v === priorityId);
  return entry ? formatEnumLabel(entry[0]) : "Unknown";
};
