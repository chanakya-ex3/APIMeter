const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;

// Enable CORS for localhost:8080
app.use(cors({
  origin: 'http://localhost:8080'
}));

// Enable body parsing for JSON and urlencoded
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Dummy endpoint 1 - 100ms latency
app.get('/api/fast', async (req, res) => {
  console.log('Hit /api/fast');
  setTimeout(() => {
    res.json({ message: 'Fast response (100ms)' });
  }, 100);
});

// Dummy endpoint 2 - 500ms latency
app.get('/api/medium', async (req, res) => {
  console.log('Hit /api/medium');
  setTimeout(() => {
    res.json({ message: 'Medium response (500ms)' });
  }, 500);
});

// Dummy endpoint 3 - 1000ms latency
app.get('/api/slow', async (req, res) => {
  console.log('Hit /api/slow');
  setTimeout(() => {
    res.json({ message: 'Slow response (1000ms)' });
  }, 1000);
});

// Dummy endpoint 4 - 2000ms latency
app.get('/api/very-slow', async (req, res) => {
  console.log('Hit /api/very-slow');
  setTimeout(() => {
    res.json({ message: 'Very slow response (2000ms)' });
  }, 2000);
});

app.listen(port, () => {
  console.log(`Express backend listening on port ${port}`);

});