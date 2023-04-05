
// <!-- Minyi Li, ml3754@drexel.edu -->
// <!-- CS530: DUI, Assignment [2] -->



function RentView() {
    var self = this;
    this.bikes = [];

    // Load data from the server
    $.get("/api/get_bikes", function(data) {
        self.bikes = data;
        self.render();
    });

    // Render the table
    this.render = function() {
        var table = $("<table>");
        var header = $("<tr>").append(
        $("<th>").text("Image"),
        $("<th>").text("Name"),
        $("<th>").text("Available"),
        $("<th>").append($("<button>").text("Reset").click(function() {
            $.post("/api/reset_bikes", {available: 3}, function() { // Bind the "Reset" button
                self.bikes.forEach(function(bike) {
                    bike.available = 3;
                });
                self.render();
            });
            })),

        $("<th>")
        );

        table.append(header);

        $.each(self.bikes, function(i, bike) {
            var row = $("<tr>").append(
                $("<td>").append('<tr><td><img src="/static/img/bikes/'+ bike.image + '" alt="sss" width="100" height="100"></td></tr>'),
                $("<td>").text(bike.name),
                $("<td>").text(bike.available),
                $("<td>").append( 
                    $("<button>").text("-").click(function() {
                        if (bike.available > 0) {
                            bike.available--;
                            self.updateBike(bike);
                            self.render();
                            $.post("/api/update_bike", {id: bike.id, available: bike.available});
                        }
                    }),
                    $("<button>").text("+").click(function() {
                        bike.available++;
                        self.updateBike(bike);
                        self.render();
                    })
                )
            );

            // if unavailable, set the row to opacity 0.25 and disable the ‘–’ button
            if (bike.available == 0) {
                row.css("opacity", ".25");
                row.find("button").prop("disabled", true);
            }

                table.append(row);
        });

        $("#bikes-table").html(table);
    };

    // Update the availability of a given bike
    this.updateBike = function(bike) {
        $.post("/api/update_bike", {id: bike.id, available: bike.available});
    };



    // Bind the "Reset" button
    $("#resetButton").click(function() {
        self.resetBikes();
    });


 }

// Instantiate the RentView object
var rentView = new RentView();




