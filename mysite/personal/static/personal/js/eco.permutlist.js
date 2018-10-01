//Function which will create the sequence which teams will appear on each round

function teamsPermutation() {
	
    var current = 0;
	var t;
	var teams = new Array("Κόκκινη", "Κίτρινη", "Μπλε");
	var teams2d = new Array(
	["Κόκκινη", "Κίτρινη", "Μπλε"],
	["Κίτρινη", "Μπλε", "Κόκκινη"],
	["Μπλε", "Κόκκινη", "Κίτρινη"],
	["Κόκκινη", "Μπλε", "Κίτρινη"],
	["Μπλε", "Κίτρινη", "Κόκκινη"],
	["Κίτρινη", "Κόκκινη", "Μπλε"],
	["Κόκκινη", "Κίτρινη", "Μπλε"],
	["Κίτρινη", "Μπλε", "Κόκκινη"],
	["Μπλε", "Κόκκινη", "Κίτρινη"],
	["Κόκκινη", "Μπλε", "Κίτρινη"]
	);
	var teamLabels = new Array("slotLabel1", "slotLabel2", "slotLabel3");
	var e = Math.floor(Math.random() * 3);  

	for (t = 0; t < teams.length; t++){
		document.getElementById(teamLabels[t]).innerHTML = "Ποσότητα για την " + teams2d[current][t] + " ddομάδα";
		current++;
		//alert(t + " " + current)
	}
    return;
  }