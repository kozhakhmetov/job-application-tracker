import { Injectable } from '@angular/core';
import {MainService} from './main.service';
import {HttpClient} from '@angular/common/http';
import {IAuthResponse, ICompany} from '../models/models';

@Injectable({
  providedIn: 'root'
})
export class ProviderService extends MainService {

  constructor(http: HttpClient) {
    super(http);
  }

  createCompany(companyName: any): Promise<ICompany> {
    return this.post('http://localhost:8000/api/company/', {
      name : companyName
    });
  }


  auth(newLogin: any, newPassword: any): Promise<IAuthResponse> {
    return this.post('http://localhost:8000/api/login/', {
      username: newLogin,
      password: newPassword
    });
  }

  logout(): Promise<any> {
    return this.post('http://localhost:8000/api/logout/', {
    });
  }
}
