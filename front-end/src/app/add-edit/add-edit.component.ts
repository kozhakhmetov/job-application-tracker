import { Component, OnInit } from '@angular/core';
import {ProviderService} from '../services/provider.service';

@Component({
  selector: 'app-add-edit',
  templateUrl: './add-edit.component.html',
  styleUrls: ['./add-edit.component.css']
})
export class AddEditComponent implements OnInit {

  companyName: any = '';

  constructor(private provider: ProviderService) { }

  ngOnInit() {
  }

  createCompany() {
    if (this.companyName !== '') {
      this.provider.createCompany(this.companyName).then(res => {
        this.companyName = '';
        console.log('Company with name:' + res.name + 'created');
      });
    }
  }

}
