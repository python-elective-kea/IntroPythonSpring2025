const markdownServe = require('markdown-serve');
const express = require('express');
const path = require('path');

const app = express();
const port = 3000;

const mdPath = path.join(__dirname);

app.use('/', markdownServe.middleware({ 
  rootDirectory: mdPath,
  view: 'markdown-serve/views/bootstrap.html'
}));

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
