# dev_flask
Web and Microservice Development with Python and Flask

##### Flask Notes
- Set Environment Variables before run for flask app
```
$export FLASK_APP=<app_directory>
$export FLASK_ENV=development
$flask run
```


##### Flask Errors and Fixes
- _endpoint_from_view_func
  - Use flask==1.1.2 instead of 2.x 

##### Javascript Testing Framework
- [https://jestjs.io](https://jestjs.io) <br/> 

##### Vue with Flask
- Install Vue.js
  ```
  $npm install -g @vue/cli@4.5.11
  ## To update vue
  $npm i -g @vue/cli
  ```
- Initialize a new Vue project called client
  ```
  $vue create client

  Vue CLI v4.5.11
  ? Please pick a preset: (Use arrow keys)
  ❯ Default ([Vue 2] babel, eslint)
    Default (Vue 3 Preview) ([Vue 3] babel, eslint)
    Manually select features
  ```

- Run Vue Server
  ```
  $npm run serve
  ```

##### Vue Errors:
- Parsing Error (eslint issue)
  ```
  1:1  error  Parsing error: Unexpected token <
  ``` 
  Fix: </br>
  ![.eslintrc.js](https://github.com/lel99999/dev_Flask/blob/master/eslintconfig-01.png) </br>

##### Node/NPM Issues & Errors
-
