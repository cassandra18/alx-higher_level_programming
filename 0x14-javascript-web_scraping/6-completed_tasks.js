#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];

if (!apiUrl) {
  console.error('Usage: node 6-completed_tasks.js <api_url>');
  process.exit(1);
}

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode === 200) {
    const tasks = JSON.parse(body);
    const userTasksCount = {};

    tasks.forEach(task => {
      const userId = task.userId;
      const completed = task.completed;

      if (completed) {
        if (userTasksCount[userId]) {
          userTasksCount[userId]++;
        } else {
          userTasksCount[userId] = 1;
        }
      }
    });

    console.log(userTasksCount);
  } else {
    console.error(`Error: ${response.statusCode}`);
  }
});
