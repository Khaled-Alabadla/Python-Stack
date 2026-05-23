# Django Session Counter

A Django project that tracks how many times a visitor has loaded the page using session state.

## Features

- Tracks page views in the user session
- Displays a visit count and counter value
- Clears the session via `/destroy_session`
- Includes a button to reset the counter
- Includes a button to increment the counter by 2
- Supports a form to increment the counter by a custom amount

## Usage

- Refresh the home page to see the session visit counter increment.
- Visit `/destroy_session` or use the reset button to clear the session and restart counts.
- Use the `+2` button to increase the counter by 2.
- Use the custom increment form to add any desired amount.
