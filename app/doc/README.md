****Project Demo****

[Link to video demo](https://mediaspace.illinois.edu/media/t/1_aynhxmml)

****Project Proposal****

1) Describe what data is stored in the database. (Where is the data from, and what attributes and information would be stored?)

      Our data is from the U.S. Department of Transportation’s Bureau of Transportation Statistics. The information stored consists of airport IATA codes, airlines, and the number of on-time, delayed, or canceled domestic flights in 2015. Other information in this database are the dates of the flights, and origin/destination airports.

2) What are the basic functions of your web application? (What can users of this website do? Which simple and complex features are there?)

- Users can enter different information about their flight (airline, airports, countries, etc.) to find the average delay time (for both arrival and departure delays) and probability of delay. 

- Users can also enter information to find the average amount of delay.

- Given two airports from the user, we will return the airline with the least probability of delay, along with the average delay time.

- The user can enter their location (latitude and longitude) and destination and see the 5 closest airports with airlines that fly to the destination, as well as the average delay for each airline.

- Users can add reviews about their experiences with airlines

- Users can update their review of an airline, given the primary key.

- Users can delete their review of an airline, given the primary key.

3) What would be a good creative component (function) that can improve the functionality of your application? (What is something cool that you want to include? How are you planning to achieve it?)

      Given information from the user (time of travel) we will return the probability of a delay occurring. We are planning on using a historical weather API to present a relationship between weather and delays through some sort of visualization, then calculating the probability of a delay based on that.

4) Project Title

      Chance My Flight

5) Project Summary:  It should be a 1-2 paragraph description of what your project is.

      Based on the time delays and cancellations data, our project provides users with predictions on the possibility of delays and cancellations for their own traveling. The durations for those delays/cancellation are also shown to users.

      For example, if one wants to travel from airport A to airport B in January, then our application would give users the shortest possible time for his/her flight, the  possibility for their flight to be canceled, and the best airline to fly on. Users can also see alternate airports they can fly from based on their location and destination.

      For the creative components, we want to directly provide the users a specific probability of delay using a weather component to find how often a flight is delayed given a certain weather condition.

6) Description of an application of your choice. State as clearly as possible what you want to do. What problem do you want to solve, etc.?

      We are planning on building a Flask application that will include information about all delayed or canceled domestic flights from 2015. Our app will have an option for users to include their origin and destination airport and we will give them the probability that their flight will be delayed. We also want to be able to tell users which airline would cause the least delay or chance of cancellation. The problem that we hope to solve is helping users choose the best airline based on their origin and destination so that they have the highest chance of reaching their destination without cancellation or a late flight.

7) Usefulness. Explain as clearly as possible why your chosen application is useful.  Make sure to answer the following questions: Are there any similar websites/applications out there?  If so, what are they, and how is yours different?

      Our application is useful because it allows users to check the probability of their flight being delayed before booking while also giving them information about the best airline to fly on based on their destination and origin as well. We weren’t able to find any websites that would calculate the probability of delay or any websites that recommended an airline based on a user’s specifications. 

8) Realness.  Describe what your data is and where you will get it.

      Our data is all delayed or canceled domestic flights in the United States in 2015 and is from the DOT’s Department of Statistics. We will include delayed flight dates, airlines, origin/destination airports, delay time, and delay cause.

9) Description of the functionality that your website offers. This is where you talk about what the website delivers. Talk about how a user would interact with the application (i.e., things that one could create, delete, update, or search for). Read the requirements for stages 4 and 5 to see what other functionalities you want to provide to the users. You should include:


- A low-fidelity UI mockup: What do you imagine your final application’s interface might look like? A PowerPoint slide or a pencil sketch on a piece of paper works!
https://docs.google.com/presentation/d/1DHW1WJx6u9kWdtHp-RM15Bu3DKYPq-Q5u9DuuIu2MqU/edit?usp=sharing 

- Project work distribution: Who would be responsible for each of the tasks or subtasks? List of the person responsible for which exact functionalities in section 6. Explain how backend systems will be distributed across members. Be as specific as possible as this could be part of the final peer evaluation metrics.

  - Kelsi: CRUD Operations, Working on UI and visual appeal
  - Ashley: Database Creation, Creating forms
  - Ishq: SQL Queries, Displaying results of queries
  - Zhuohao: Frontend-Backend Communication, Creating visualizations
 
- Functionality:
  - Users can insert records: information regarding their own flight delays
  - Users can update records: change information they previously added
  - Users can delete records: delete information they added regarding flight delays
  - Users can search the database: find specific delay information based on airline/airports/etc.
  - Advanced Queries:
    - Suggesting an airline given two airports from users based on least probability of delay, along with the average delay time and reason for delay.
    - Users can enter information about their flight (airline, origin/destination airports, etc.) to see probability of delay and average delay time.

