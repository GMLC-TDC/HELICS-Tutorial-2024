import helics as h

time = 40

broker = h.helicsCreateBroker("zmq", "main_broker", "--federates 1")

# fed = h.helicsCreateValueFederateFromConfig("config.json")
fed = h.helicsCreateCombinationFederateFromConfig("config.json")

input_ID = h.helicsFederateGetInputByTarget(fed, "AnotherFederate/test_subscription")
pub_ID = h.helicsFederateGetPublication(fed, "test_publication")
endpoint_ID = h.helicsFederateGetEndpoint(fed, "test_endpoint")

input_key = h.helicsInputGetTarget(input_ID)
pub_key = h.helicsPublicationGetName(pub_ID)
endpoint_name = h.helicsEndpointGetName(endpoint_ID)

h.helicsFederateEnterExecutingMode(fed)
grantedtime = h.helicsFederateRequestTime(fed, time)
float_value = h.helicsInputGetDouble(input_ID)
h.helicsPublicationPublishDouble(pub_ID, float_value)

h.helicsFederateDisconnect(fed)
h.helicsFederateFree(fed)
h.helicsCloseLibrary()
