# RentBike

This assignment asks you to continue developing your website for “Drexel Bikes”, specifically in adding several features to make it a more realistic site—receiving data from a live database and allowing the user to view and change this information.
The implementation of our “Drexel Bikes” website for Assignment 1 built the basic styling and navigation bar for the site and added a page “Our Bikes” where the user could see the list of available bikes. In this assignment, we will enhance this site to include a live SQLite database. 

“Rent a Bike” Page

create a page that generates dynamic content, using JavaScript to populate the page table and handle events on the page. On this page, the user sees the number of bikes available for each bike. The user can click on ‘–’ to decrease this number and ‘+’ to increase this number. If the number of bikes reaches 0, the row should be grayed out, and the ‘–’ button should no longer work (so that the number cannot go below 0). If the user clicks the “Reset” button at the top of the table, the available number for *all* bikes should be set to 3. 
Next, create a file rentView.js that builds the “view” for this page, namely the main table that includes all the bikes with their availability. We recommend creating a JavaScript object RentView, using the function RentView(..) { .. } and then instantiating the object with a new RentView(..). In this object, you can implement the necessary functionality to: (1) load data from the server, (2) change the availability of a given bike, and (3) reset all bikes to have the same availability (namely 3). For each of these functions, you will also need to implement the corresponding functionality on the server side in the run.py file. Specifically, should define the API URLs with associated AJAX functionality. The final page should provide all the functionality of the buttons described above, and since having a database back end, all data should remain the same even after reloading the page.

![effb2ad7955fe6e4f1405fadf8525b7](https://user-images.githubusercontent.com/56332687/230013521-d9fe99b4-4844-4985-8f3c-79b8ca1f2f71.png)
![b1d1a06f0f55e23f060dfebf968f8f6](https://user-images.githubusercontent.com/56332687/230013528-a88592d3-c11f-409a-9f06-809de46717e3.png)
