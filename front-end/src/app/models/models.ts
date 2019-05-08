export interface IAuthResponse {
  token: string;
}

export interface ICompany {
  name: string;
}

export interface IPosition {
  name: string;
  link: string;
  location: string;
  company: ICompany;
  type: string;
}

export interface IUserApplication {
  position: IPosition;
  status: IStatus;
  comment: string;
  recruiter_contact: string;
  applied_at: string;
}

export interface IStatus {
  name: string;
}

export interface ISchedule {
  event_type: string;
  date: string;
}
