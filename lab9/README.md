![alt text](1.PNG)

##rs.status()
```
{
	"set" : "rs0",
	"date" : ISODate("2019-10-31T23:07:12.422Z"),
	"myState" : 1,
	"term" : NumberLong(1),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572563215, 1),
			"t" : NumberLong(1)
		},
		"lastCommittedWallTime" : ISODate("2019-10-31T23:06:55.040Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572563215, 1),
			"t" : NumberLong(1)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-31T23:06:55.040Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572563215, 1),
			"t" : NumberLong(1)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572563215, 1),
			"t" : NumberLong(1)
		},
		"lastAppliedWallTime" : ISODate("2019-10-31T23:06:55.040Z"),
		"lastDurableWallTime" : ISODate("2019-10-31T23:06:55.040Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572544399, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572544399, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "electionTimeout",
		"lastElectionDate" : ISODate("2019-10-31T17:53:19.041Z"),
		"termAtElection" : NumberLong(1),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(0, 0),
			"t" : NumberLong(-1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572544430, 1),
			"t" : NumberLong(-1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-31T17:53:19.142Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T17:53:50.020Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1:27017",
			"ip" : "172.31.53.56",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 102551,
			"optime" : {
				"ts" : Timestamp(1572563215, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-31T23:06:55Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572544429, 1),
			"electionDate" : ISODate("2019-10-31T17:53:19Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 1,
			"name" : "db2:27017",
			"ip" : "172.31.48.173",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 101903,
			"optime" : {
				"ts" : Timestamp(1572563215, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572563215, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-31T23:06:55Z"),
			"optimeDurableDate" : ISODate("2019-10-31T23:06:55Z"),
			"lastHeartbeat" : ISODate("2019-10-31T22:20:25.883Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T22:20:25.883Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db1:27017",
			"syncSourceHost" : "db1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		},
		{
			"_id" : 3,
			"name" : "db3:27017",
			"ip" : "172.31.48.65",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 101903,
			"optime" : {
				"ts" : Timestamp(1572563215, 1),
				"t" : NumberLong(1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572563215, 1),
				"t" : NumberLong(1)
			},
			"optimeDate" : ISODate("2019-10-31T23:06:55Z"),
			"optimeDurableDate" : ISODate("2019-10-31T23:06:55Z"),
			"lastHeartbeat" : ISODate("2019-10-31T22:20:25.534Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T22:20:25.534Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db1:27017",
			"syncSourceHost" : "db1:27017",
			"syncSourceId" : 0,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572563215, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572563215, 1)
}
```
##rs.config()
```
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "db1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "db2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 3,
			"host" : "db3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("67px206d4apfg8a0295agh0c")
	}
}
```

![alt text](2.PNG)

##rs.status()
```
{
	"set" : "rs0",
	"date" : ISODate("2019-10-31T23:15:44.427Z"),
	"myState" : 1,
	"term" : NumberLong(2),
	"syncingTo" : "",
	"syncSourceHost" : "",
	"syncSourceId" : -1,
	"heartbeatIntervalMillis" : NumberLong(2000),
	"majorityVoteCount" : 2,
	"writeMajorityCount" : 2,
	"optimes" : {
		"lastCommittedOpTime" : {
			"ts" : Timestamp(1572563736, 1),
			"t" : NumberLong(2)
		},
		"lastCommittedWallTime" : ISODate("2019-10-31T23:15:36.060Z"),
		"readConcernMajorityOpTime" : {
			"ts" : Timestamp(1572563736, 1),
			"t" : NumberLong(2)
		},
		"readConcernMajorityWallTime" : ISODate("2019-10-31T23:15:36.060Z"),
		"appliedOpTime" : {
			"ts" : Timestamp(1572563736, 1),
			"t" : NumberLong(2)
		},
		"durableOpTime" : {
			"ts" : Timestamp(1572563736, 1),
			"t" : NumberLong(2)
		},
		"lastAppliedWallTime" : ISODate("2019-10-31T23:15:36.060Z"),
		"lastDurableWallTime" : ISODate("2019-10-31T23:15:36.060Z")
	},
	"lastStableRecoveryTimestamp" : Timestamp(1572563765, 1),
	"lastStableCheckpointTimestamp" : Timestamp(1572563765, 1),
	"electionCandidateMetrics" : {
		"lastElectionReason" : "stepUpRequestSkipDryRun",
		"lastElectionDate" : ISODate("2019-10-31T23:16:05.488Z"),
		"termAtElection" : NumberLong(2),
		"lastCommittedOpTimeAtElection" : {
			"ts" : Timestamp(1572563751, 1),
			"t" : NumberLong(1)
		},
		"lastSeenOpTimeAtElection" : {
			"ts" : Timestamp(1572563751, 1),
			"t" : NumberLong(1)
		},
		"numVotesNeeded" : 2,
		"priorityAtElection" : 1,
		"electionTimeoutMillis" : NumberLong(10000),
		"priorPrimaryMemberId" : 0,
		"numCatchUpOps" : NumberLong(27017),
		"newTermStartDate" : ISODate("2019-10-31T23:15:50.057Z"),
		"wMajorityWriteAvailabilityDate" : ISODate("2019-10-31T23:15:52.293Z")
	},
	"members" : [
		{
			"_id" : 0,
			"name" : "db1:27017",
			"ip" : "172.31.53.56",
			"health" : 0,
			"state" : 8,
			"stateStr" : "(not reachable/healthy)",
			"uptime" : 0,
			"optime" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDurable" : {
				"ts" : Timestamp(0, 0),
				"t" : NumberLong(-1)
			},
			"optimeDate" : ISODate("1970-01-01T00:00:00Z"),
			"optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
			"lastHeartbeat" : ISODate("2019-10-31T23:16:22.508Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T23:16:05.913Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "Error connecting to db1:27017 (172.31.53.56:27017) :: caused by :: Connection refused",
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"configVersion" : -1
		},
		{
			"_id" : 1,
			"name" : "db2:27017",
			"ip" : "172.31.48.173",
			"health" : 1,
			"state" : 1,
			"stateStr" : "PRIMARY",
			"uptime" : 103128,
			"optime" : {
				"ts" : Timestamp(1572563736, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-31T23:16:12Z"),
			"syncingTo" : "",
			"syncSourceHost" : "",
			"syncSourceId" : -1,
			"infoMessage" : "",
			"electionTime" : Timestamp(1572563765, 1),
			"electionDate" : ISODate("2019-10-31T23:16:05Z"),
			"configVersion" : 1,
			"self" : true,
			"lastHeartbeatMessage" : ""
		},
		{
			"_id" : 3,
			"name" : "db3:27017",
			"ip" : "172.31.48.65",
			"health" : 1,
			"state" : 2,
			"stateStr" : "SECONDARY",
			"uptime" : 102502,
			"optime" : {
				"ts" : Timestamp(1572563736, 1),
				"t" : NumberLong(2)
			},
			"optimeDurable" : {
				"ts" : Timestamp(1572563736, 1),
				"t" : NumberLong(2)
			},
			"optimeDate" : ISODate("2019-10-31T23:16:12Z"),
			"optimeDurableDate" : ISODate("2019-10-31T23:16:12Z"),
			"lastHeartbeat" : ISODate("2019-10-31T23:16:05.534Z"),
			"lastHeartbeatRecv" : ISODate("2019-10-31T23:15:44.318Z"),
			"pingMs" : NumberLong(0),
			"lastHeartbeatMessage" : "",
			"syncingTo" : "db2:27017",
			"syncSourceHost" : "db2:27017",
			"syncSourceId" : 1,
			"infoMessage" : "",
			"configVersion" : 1
		}
	],
	"ok" : 1,
	"$clusterTime" : {
		"clusterTime" : Timestamp(1572563736, 1),
		"signature" : {
			"hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
			"keyId" : NumberLong(0)
		}
	},
	"operationTime" : Timestamp(1572563736, 1)
}
```
##rs.config()
```
{
	"_id" : "rs0",
	"version" : 1,
	"protocolVersion" : NumberLong(1),
	"writeConcernMajorityJournalDefault" : true,
	"members" : [
		{
			"_id" : 0,
			"host" : "db1:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 1,
			"host" : "db2:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		},
		{
			"_id" : 3,
			"host" : "db3:27017",
			"arbiterOnly" : false,
			"buildIndexes" : true,
			"hidden" : false,
			"priority" : 1,
			"tags" : {
				
			},
			"slaveDelay" : NumberLong(0),
			"votes" : 1
		}
	],
	"settings" : {
		"chainingAllowed" : true,
		"heartbeatIntervalMillis" : 2000,
		"heartbeatTimeoutSecs" : 10,
		"electionTimeoutMillis" : 10000,
		"catchUpTimeoutMillis" : -1,
		"catchUpTakeoverDelayMillis" : 30000,
		"getLastErrorModes" : {
			
		},
		"getLastErrorDefaults" : {
			"w" : 1,
			"wtimeout" : 0
		},
		"replicaSetId" : ObjectId("67px206d4apfg8a0295agh0c")
	}
}
```

