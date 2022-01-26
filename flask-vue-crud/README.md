##### Setup Instructions
- Vue Setup
  ```
  $npm i -g @vue/cli@4.5.11
  ## to update vue
  $npm i -g @vue/cli
  ```

- Initialize a new Vue Project
  ```
  $vue create <project_name>
  ```
  - this will require answering a few questions
    ```
    Vue CLI v4.5.11
    ? Please pick a preset: Manually select features
    ? Check the features needed for your project:
    ❯◉ Choose Vue version
     ◉ Babel
     ◯ TypeScript
     ◯ Progressive Web App (PWA) Support
     ◉ Router
     ◯ Vuex
     ◯ CSS Pre-processors
     ◉ Linter / Formatter
     ◯ Unit Testing
     ◯ E2E Testing

     Press Enter.

     Select "2.x" for the Vue version. Use the history mode for the router. Select "ESLint + Airbnb config"
     for the linter and "Lint on save". Finally, select the "In package.json" option so that configuration
     is placed in the package.json file instead of in separate configuration files.

     You should see something similar to:

     Vue CLI v4.5.11
     ? Please pick a preset: Manually select features
     ? Check the features needed for your project: Choose Vue version, Babel, Router, Linter
     ? Choose a version of Vue.js that you want to start the project with 2.x
     ? Use history mode for router? (Requires proper server setup for index fallback in production) Yes
     ? Pick a linter / formatter config: Airbnb
     ? Pick additional lint features: Lint on save
     ? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
     ? Save this as a preset for future projects? (y/N) No

     Press enter again to configure the project structure and install the dependencies.
     ``` 
