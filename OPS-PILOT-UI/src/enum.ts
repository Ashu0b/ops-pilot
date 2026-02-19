// enum.ts
export const EventStatusEnum = {
  OPEN: 1,
  IN_PROGRESS: 2,
  RESOLVED: 3,
  CLOSED: 4,
} as const;

export type EventStatusEnum =
  (typeof EventStatusEnum)[keyof typeof EventStatusEnum];

export const PriorityEnum = {
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
  CRITICAL: 4,
} as const;

export type PriorityEnum = (typeof PriorityEnum)[keyof typeof PriorityEnum];
