import { Component } from '@angular/core';

@Component({
  selector: 'ngx-footer',
  styleUrls: ['./footer.component.scss'],
  template: `
    <span class="created-by">
      Created by by <b><a href="https://github.com/Danylo79" target="_blank">Danylo Komisarenko</a></b> 2022
    </span>
    <div class="socials">
      <a href="https://github.com/Danylo79/ClassEconomy" target="_blank" class="ion ion-social-github"></a>
    </div>
  `,
})
export class FooterComponent {
}
