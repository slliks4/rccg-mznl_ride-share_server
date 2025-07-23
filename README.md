# Ride Share MVP

## Session 
Store recurrence patterns and generates recurring events
i.e (Sunday service, Tuesday service, Thursday service (with recurring pattern)),
Sisters' conference 2025 {
    Friday, august 1st 2025, (6pm-8pm)
    Saturday, august 2nd 2025, (12pm-4pm)
    Sunday, august 12t 2025, (10am-12pm)
}

### Session Model
* title (Char Field): Represents the name of the session (e.g., "Sunday Service"). 
* recurring (Boolean Field): default=False
* recurrence_pattern: interval (Select field: yearly, montly, weekly), end(type: "never" // or "on": "2029-08-03" or "after": 5 (occurrences)
* dates: days(sunday-monday), month: (1-12), day_of_month: (usually 1-31, depends on the month and year, taking account of leap years), time_start: (time-field), time_end: (time-field)


## Events
Represent a bookable instance, even if it's generated from a recurring pattern

### Event Model:


what we want to cover,
1. Recurring events
When a session or event is created it has a boolean for recurring which has a customizable date structure. Custom recurrence using a simler structure to google calendar create event. field described more in the session model
2. Events or Conference that spans over days: This also makes use of the custom recurrence, where an event can spam across different days in different time
3. Normal single day events: Just an event for a single day

So, what the logic I am aiming for is pretty simple, I don't want to clutter the ui with recurring events since they are basically thesame thing, so the ui can just be focused on future events with recurring be grouped, but then when a user wants to book a ride for one of the recurring events, it then has a drop down on where the user can then book what particular event under the recurring, buthen I want it to contain an absolute which is similar to recurring but then this are constant so it doesn't make sense to have a drop down for example every sunday in a year, it doesn't make sense to list that out, so instead absolute allows user to be able to only book ride to an upcoming sunday only,

or I can just go through the more easier route by forgetting about recurring and just creating each events for a particular week andincluding a schedule, so the ui only shows events for a week or events with priority set with true, that way I can just do it like scheduling, create all events and group by week and by default it just shows events for that week which user can request a ride for, but then I can also have a priority group which are always showned and these are for special programs we want maybe people to start booking



