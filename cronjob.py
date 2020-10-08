import requests
import csv
import json

# Automation of telescope data with scrapping
#collections = ['CFHT', 'CFHTMEGAPIPE', 'CFHTTERAPIX', 'CFHTWIRWOLF', 'HST', 'HSTHLA', 'GEMINI', 'JCMT', 'JCMTLS', 'DAO', 'DAOPLATES', 'MACHO', 'DRAO', 'BLAST', 'VGPS', 'VLASS', 'FUSE', 'TESS', 'MOST', 'IRIS', 'APASS', 'NGVS', 'SDSS', 'CHANDRA', 'OMM', 'XMM', 'CGPS', 'NEOSSAT', 'SUBARU', 'NOAO', 'UKIRT']
collections = ["BLAST"]
with open("./upload/data/json_db.json", "w+") as json_db:
    print("[Check] Reading the JSON file...")
    if not json_db.read():
        print("[Check] JSON file is empty, creating a blank dictionary...")
        _json = {}
    else:
        print("[Check] JSON file isn't empty, using it...")
        _json = json.loads(json_db.read())
    print("[OK] JSON file loaded...")
    print("[Check] Starting to iterate on the telescope array...")
    for coll in collections:
        print("[Check] Iterating over {0} telescope".format(coll))
        csv_file = open("./upload/data/buffer.csv", "w+") # Not effective
        print("[OK] Buffer file initialized...")
        print("[Check] Probing CADC archives...")
        csv_file.write(requests.get(r"https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/argus/sync?LANG=ADQL&REQUEST=doQuery&QUERY=SELECT%20Observation.observationURI%20AS%20%22Preview%22%2C%20Observation.collection%20AS%20%22Collection%22%2C%20Observation.observationID%20AS%20%22Obs.%20ID%22%2C%20Plane.productID%20AS%20%22Product%20ID%22%2C%20COORD1(CENTROID(Plane.position_bounds))%20AS%20%22RA%20(J2000.0)%22%2C%20COORD2(CENTROID(Plane.position_bounds))%20AS%20%22Dec.%20(J2000.0)%22%2C%20Plane.time_bounds_lower%20AS%20%22Start%20Date%22%2C%20Observation.instrument_name%20AS%20%22Instrument%22%2C%20Plane.time_exposure%20AS%20%22Int.%20Time%22%2C%20Observation.target_name%20AS%20%22Target%20Name%22%2C%20Plane.energy_bandpassName%20AS%20%22Filter%22%2C%20Plane.calibrationLevel%20AS%20%22Cal.%20Lev.%22%2C%20Observation.type%20AS%20%22Obs.%20Type%22%2C%20Plane.energy_bounds_lower%20AS%20%22Min.%20Wavelength%22%2C%20Plane.energy_bounds_upper%20AS%20%22Max.%20Wavelength%22%2C%20Observation.proposal_id%20AS%20%22Proposal%20ID%22%2C%20Observation.proposal_pi%20AS%20%22P.I.%20Name%22%2C%20Plane.dataRelease%20AS%20%22Data%20Release%22%2C%20AREA(Plane.position_bounds)%20AS%20%22Field%20of%20View%22%2C%20Plane.position_bounds%20AS%20%22Shape%22%2C%20Plane.position_sampleSize%20AS%20%22Pixel%20Scale%22%2C%20Plane.energy_resolvingPower%20AS%20%22Resolving%20Power%22%2C%20Plane.time_bounds_upper%20AS%20%22End%20Date%22%2C%20Plane.dataProductType%20AS%20%22Data%20Type%22%2C%20Observation.target_moving%20AS%20%22Moving%20Target%22%2C%20Plane.provenance_name%20AS%20%22Provenance%20Name%22%2C%20Plane.provenance_keywords%20AS%20%22Provenance%20Keywords%22%2C%20Observation.intent%20AS%20%22Intent%22%2C%20Observation.target_type%20AS%20%22Target%20Type%22%2C%20Observation.target_standard%20AS%20%22Target%20Standard%22%2C%20Observation.target_keywords%20AS%20%22Target%20Keywords%22%2C%20Plane.metaRelease%20AS%20%22Meta%20Release%22%2C%20Observation.sequenceNumber%20AS%20%22Sequence%20Number%22%2C%20Observation.algorithm_name%20AS%20%22Algorithm%20Name%22%2C%20Observation.proposal_title%20AS%20%22Proposal%20Title%22%2C%20Observation.proposal_keywords%20AS%20%22Proposal%20Keywords%22%2C%20Plane.position_resolution%20AS%20%22IQ%22%2C%20Observation.instrument_keywords%20AS%20%22Instrument%20Keywords%22%2C%20Observation.environment_tau%20AS%20%22Tau%22%2C%20Plane.energy_transition_species%20AS%20%22Molecule%22%2C%20Plane.energy_transition_transition%20AS%20%22Transition%22%2C%20Observation.proposal_project%20AS%20%22Proposal%20Project%22%2C%20Plane.energy_emBand%20AS%20%22Band%22%2C%20Plane.provenance_reference%20AS%20%22Prov.%20Reference%22%2C%20Plane.provenance_version%20AS%20%22Prov.%20Version%22%2C%20Plane.provenance_project%20AS%20%22Prov.%20Project%22%2C%20Plane.provenance_producer%20AS%20%22Prov.%20Producer%22%2C%20Plane.provenance_runID%20AS%20%22Prov.%20Run%20ID%22%2C%20Plane.provenance_lastExecuted%20AS%20%22Prov.%20Last%20Executed%22%2C%20Plane.provenance_inputs%20AS%20%22Prov.%20Inputs%22%2C%20Plane.energy_restwav%20AS%20%22Rest-frame%20Energy%22%2C%20Observation.requirements_flag%20AS%20%22Quality%22%2C%20Plane.planeID%20AS%20%22planeID%22%2C%20isDownloadable(Plane.publisherID)%20AS%20%22DOWNLOADABLE%22%2C%20Plane.publisherID%20AS%20%22Publisher%20ID%22%20FROM%20caom2.Plane%20AS%20Plane%20JOIN%20caom2.Observation%20AS%20Observation%20ON%20Plane.obsID%20%3D%20Observation.obsID%20WHERE%20%20(%20Observation.collection%20%3D%20%27{0}%27%20AND%20%20(%20Plane.quality_flag%20IS%20NULL%20OR%20Plane.quality_flag%20%21%3D%20%27junk%27%20)%20)&FORMAT=csv".format(coll)).content.decode("utf-8"))
        print("[OK] Probe successfull!")
        with open("buffer.csv", "r+") as file:
            print("[OK] Reading the buffer file...")
            csvReader = csv.DictReader(file)
            print("[OK] CSVReader initialized...")
            targets = []
            print("[Check] Starting to iterate on the csv (target_name row)...")
            for rows in csvReader:
                print("\r[Check] Iterating over {0} target...".format(rows['"Target Name"']))
                print("\r[Check] Probing Simbad archives...")
                r = requests.get("http://simbad.u-strasbg.fr/simbad/sim-id?output.format=ASCII&Ident={0}&output.params=main_id".format(rows['"Target Name"']))
                print("[OK] Probe successfull!")
                if not r.text[:2] == "!!":
                    targets.append(r.text.split("\n")[2])
            print("[OK] Iteration over for {0} telescope's rows".format(coll))
            targets = set(targets)
            print(targets)
            try:
                print("[OK] Found an existing telescope entry, appending new data...")
                for target in targets:
                    if not target in _json[coll]:
                        print("[Check] Appending {0} as a new data...".format(target))
                        _json[coll] = [*_json[coll], target]
                        print("[OK] Append successfull")
            except KeyError as e:
                print("[Error] No telescope entry found, creating a new one...")
                _json[coll] = [*targets]
                print("[OK] Created a new telescope column...")
    print("[OK] Iteration over for telescopes...")
    json_db.write(json.dumps(_json))
# https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/en/search/?Plane.position.bounds@Shape1Resolver.value=ALL&Observation.collection=BLAST#sortCol=caom2%3APlane.time.bounds.lower&sortDir=dsc&col_1=_checkbox_selector;;;&col_2=caom2%3AObservation.uri;;;&col_3=caom2%3AObservation.collection;;;&col_4=caom2%3AObservation.observationID;;;&col_5=caom2%3APlane.productID;;;&col_6=caom2%3APlane.position.bounds.cval1;;;&col_7=caom2%3APlane.position.bounds.cval2;;;&col_8=caom2%3APlane.time.bounds.lower;;;&col_9=caom2%3AObservation.instrument.name;;;&col_10=caom2%3APlane.time.exposure;;;&col_11=caom2%3AObservation.target.name;;;&col_12=caom2%3APlane.energy.bandpassName;;;&col_13=caom2%3APlane.calibrationLevel;;;&col_14=caom2%3AObservation.type;;;
# https://www.cadc-ccda.hia-iha.nrc-cnrc.gc.ca/argus/sync?LANG=ADQL&REQUEST=doQuery&QUERY=SELECT%20Observation.observationURI%20AS%20%22Preview%22%2C%20Observation.collection%20AS%20%22Collection%22%2C%20Observation.observationID%20AS%20%22Obs.%20ID%22%2C%20Plane.productID%20AS%20%22Product%20ID%22%2C%20COORD1(CENTROID(Plane.position_bounds))%20AS%20%22RA%20(J2000.0)%22%2C%20COORD2(CENTROID(Plane.position_bounds))%20AS%20%22Dec.%20(J2000.0)%22%2C%20Plane.time_bounds_lower%20AS%20%22Start%20Date%22%2C%20Observation.instrument_name%20AS%20%22Instrument%22%2C%20Plane.time_exposure%20AS%20%22Int.%20Time%22%2C%20Observation.target_name%20AS%20%22Target%20Name%22%2C%20Plane.energy_bandpassName%20AS%20%22Filter%22%2C%20Plane.calibrationLevel%20AS%20%22Cal.%20Lev.%22%2C%20Observation.type%20AS%20%22Obs.%20Type%22%2C%20Plane.energy_bounds_lower%20AS%20%22Min.%20Wavelength%22%2C%20Plane.energy_bounds_upper%20AS%20%22Max.%20Wavelength%22%2C%20Observation.proposal_id%20AS%20%22Proposal%20ID%22%2C%20Observation.proposal_pi%20AS%20%22P.I.%20Name%22%2C%20Plane.dataRelease%20AS%20%22Data%20Release%22%2C%20AREA(Plane.position_bounds)%20AS%20%22Field%20of%20View%22%2C%20Plane.position_bounds%20AS%20%22Shape%22%2C%20Plane.position_sampleSize%20AS%20%22Pixel%20Scale%22%2C%20Plane.energy_resolvingPower%20AS%20%22Resolving%20Power%22%2C%20Plane.time_bounds_upper%20AS%20%22End%20Date%22%2C%20Plane.dataProductType%20AS%20%22Data%20Type%22%2C%20Observation.target_moving%20AS%20%22Moving%20Target%22%2C%20Plane.provenance_name%20AS%20%22Provenance%20Name%22%2C%20Plane.provenance_keywords%20AS%20%22Provenance%20Keywords%22%2C%20Observation.intent%20AS%20%22Intent%22%2C%20Observation.target_type%20AS%20%22Target%20Type%22%2C%20Observation.target_standard%20AS%20%22Target%20Standard%22%2C%20Observation.target_keywords%20AS%20%22Target%20Keywords%22%2C%20Plane.metaRelease%20AS%20%22Meta%20Release%22%2C%20Observation.sequenceNumber%20AS%20%22Sequence%20Number%22%2C%20Observation.algorithm_name%20AS%20%22Algorithm%20Name%22%2C%20Observation.proposal_title%20AS%20%22Proposal%20Title%22%2C%20Observation.proposal_keywords%20AS%20%22Proposal%20Keywords%22%2C%20Plane.position_resolution%20AS%20%22IQ%22%2C%20Observation.instrument_keywords%20AS%20%22Instrument%20Keywords%22%2C%20Observation.environment_tau%20AS%20%22Tau%22%2C%20Plane.energy_transition_species%20AS%20%22Molecule%22%2C%20Plane.energy_transition_transition%20AS%20%22Transition%22%2C%20Observation.proposal_project%20AS%20%22Proposal%20Project%22%2C%20Plane.energy_emBand%20AS%20%22Band%22%2C%20Plane.provenance_reference%20AS%20%22Prov.%20Reference%22%2C%20Plane.provenance_version%20AS%20%22Prov.%20Version%22%2C%20Plane.provenance_project%20AS%20%22Prov.%20Project%22%2C%20Plane.provenance_producer%20AS%20%22Prov.%20Producer%22%2C%20Plane.provenance_runID%20AS%20%22Prov.%20Run%20ID%22%2C%20Plane.provenance_lastExecuted%20AS%20%22Prov.%20Last%20Executed%22%2C%20Plane.provenance_inputs%20AS%20%22Prov.%20Inputs%22%2C%20Plane.energy_restwav%20AS%20%22Rest-frame%20Energy%22%2C%20Observation.requirements_flag%20AS%20%22Quality%22%2C%20Plane.planeID%20AS%20%22planeID%22%2C%20isDownloadable(Plane.publisherID)%20AS%20%22DOWNLOADABLE%22%2C%20Plane.publisherID%20AS%20%22Publisher%20ID%22%20FROM%20caom2.Plane%20AS%20Plane%20JOIN%20caom2.Observation%20AS%20Observation%20ON%20Plane.obsID%20%3D%20Observation.obsID%20WHERE%20%20(%20Observation.collection%20%3D%20%27BLAST%27%20AND%20%20(%20Plane.quality_flag%20IS%20NULL%20OR%20Plane.quality_flag%20%21%3D%20%27junk%27%20)%20)&FORMAT=csv