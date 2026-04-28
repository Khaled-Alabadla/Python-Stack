# Flask Counter Application

Web application built with Flask that tracks the number of times a user has visited the page and allows manual manipulation of a session-based counter.

## Features

- **Visit Tracking**: Automatically counts how many times the root page has been loaded.
- **Incremental Counter**: A separate counter that increments with every page load.
- **Custom Increments**:
  - **+2 Points**: Button to increment the counter by 2.
  - **Custom Amount**: Form to increment the counter by any specified integer.
- **Reset Functionality**:
  - **Reset Counter**: Resets the counter back to 0 while keeping the visit history.
  - **Clear Session**: Completely clears the session, resetting both visits and the counter to 0.
