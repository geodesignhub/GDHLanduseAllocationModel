# configure the API settings with the correct project id and username
apisettings = {
  "serviceurl": "http://local.dev:8000/api/v1/",
  "projectid": "23f85c2a201b8cfb",
  "apitoken": "bf6568eeebe620616f715753b4a70bd90b07d940",
  "username": "ufeusr1",
}
# enter the correct change team and synthesis ID
changeteamandsynthesis = {
	"changeteamid": 1,
	"synthesisid":"264AH9GD48GKN6AK"
}
# enter the details of the gridded evaluation files and the correct system ID and priority.
evalsandpriority = [
	{"priority":1, "evalfilename": "input-evaluations/HDH.geojson", "systemid":35, "name":"Housing"},
	]

featurefilesandpriority = [
	{"priority":1, "systemid":35, "name":"Housing","target": 10000, "allocationtype":"cluster"},
]
units = "hectares" # can only be acres or hectares
allocationrunnumber = 0 # give a run number, it will be appended to the upload