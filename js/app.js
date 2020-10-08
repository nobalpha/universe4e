initAladin("lmc");
var json_db;
const xml = new XMLHttpRequest();
xml.open("GET", "data/json_db.json", false);
xml.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
        json_db = JSON.parse(xml.responseText);
    }
};
xml.send();

const select = document.getElementById("coll_set");
const obs_select = document.getElementById("obs_set");

for (var key in json_db) {
    var option = document.createElement("option");
    option.innerHTML = `${key}`;
    select.appendChild(option);
}

select.onchange = function(e){
    obs_select.innerHTML = "";
    for (var key of json_db[select.value]) {
        let option = document.createElement("option");
        option.innerHTML = `${key}`;
        obs_select.appendChild(option);
    }
};

obs_select.onchange = function(e) {
    initAladin(obs_select.value);
    console.log(obs_select.value);
}

function initAladin(obs) {
    let aladin = A.aladin('#aladin-lite-div', {
        target: obs
    });
    let hips = A.catalogHiPS('https://axel.u-strasbg.fr/HiPSCatService/Simbad', {
        onClick: 'showTable',
        name: obs
    });
    aladin.addCatalog(hips);

    return aladin;
}

