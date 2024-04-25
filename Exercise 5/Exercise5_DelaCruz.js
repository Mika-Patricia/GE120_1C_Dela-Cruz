/* GE 120
Mika Patricia G. Dela Cruz
2023-03941*/

function getLatitude(distance, azimuth){
     /*
    Compute for the Latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    Latitude - float
    */

    return (-distance * Math.cos(azimuth * Math.PI / 180.0));
    
}

function getDeparture(distance, azimuth){ 
    /*
    Compute for the departure of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    Departure - float
    */

 return (-distance * Math.sin(azimuth * Math.PI / 180.0));
    
}

function azimuthToBearing(azimuth) {
    /*
    Compute for the DMS bearing of a given angle.

    Input:
    azimtuh - float

    Output:
    bearing - string
    */

    let angle = (azimuth + 360) % 360; // Ensure angle is positive and within 0-360 degrees

    if (angle === 0 || angle === 360) {
        return `${0} degrees S`;
    } else if (angle === 90) {
        return `${0} degrees E`;
    } else if (angle === 180) {
        return `${0} degrees N`;
    } else if (angle === 270) {
        return `${0} degrees W`;
    } else if (angle > 0 && angle < 90) {
        return `S ${angle.toFixed(3).padStart(5)} W`;
    } else if (angle > 90 && angle < 180) {
        return `N ${(180 - angle).toFixed(3).padStart(5)} W`;
    } else if (angle > 180 && angle < 270) {
        return `N ${(angle - 180).toFixed(3).padStart(5)} E`;
    } else if (angle > 270 && angle < 360) {
        return `S ${(360 - angle).toFixed(3).padStart(5)} E`;
    } else {
        return "UNKNOWN";
    }
}

var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
];
var lines = [];
var sumLat = 0;
var sumDep = 0;
var sumDist = 0;

for (var i = 0; i < data.length; i++){
    let line = data[i];
    let distance = line[0];
    let azimuth = line[1];

    let bearing = azimuthToBearing(azimuth);
    let lat = getLatitude(distance, azimuth);
    let dep = getDeparture(distance, azimuth);

    sumLat += lat;
    sumDep += dep;
    sumDist += distance;

    lines.push([i, distance, bearing, lat, dep]);
}

console.log("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(15), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10));
for (var line of lines){
    console.log(
        line[0].toString().padEnd(10),
        line[1].toString().padEnd(10), 
        line[2].padEnd(15), 
        line[3].toFixed(5).toString().padEnd(10), 
        line[4].toFixed(5).toString().padEnd(10)
    );    
}

console.log("SUMMATION OF LAT:", sumLat.toFixed(5));
console.log("SUMMATION OF DEP:", sumDep.toFixed(5));
console.log("SUMMATION OF DIST:", sumDist.toFixed(5));

var lec = Math.sqrt(sumLat**2 + sumDep**2);

console.log("LEC", lec.toFixed(5));

var rec = sumDist / lec;

console.log("1:  ", Math.floor(rec / 1000) * 1000);

console.log("------END-------");
