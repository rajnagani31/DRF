data={
  "system": {
    "id": "SYS-999",
    "status": "running",
    "config": {
      "version": "1.2.5",
      "env": {
        "os": "Linux",
        "arch": "x86_64",
        "variables": {
          "PATH": "/usr/bin:/bin:/usr/local/bin",
          "JAVA_HOME": "/usr/lib/jvm/java-17-openjdk",
          "nestedEnv": {
            "NODE_ENV": "production",
            "DATABASE": {
              "type": "postgres",
              "credentials": {
                "user": "admin",
                "password": "secret123",
                "hosts": [
                  {"ip": "192.168.1.10", "port": 5432},
                  {"ip": "192.168.1.11", "port": 5432}
                ],
                "replicaSet": {
                  "enabled": "true",
                  "nodes": [
                    {"id": 1, "status": "active"},
                    {"id": 2, "status": "standby"}
                  ]
                }
              }
            }
          }
        }
      }
    }
  },
  "users": [
    {
      "id": 1,
      "profile": {
        "name": "Alice",
        "contacts": [
          {"type": "email", "value": "alice@example.com"},
          {"type": "phone", "value": "+91-9876543210"}
        ]
      },
      "settings": {
        "theme": "light",
        "security": {
          "2FA": "true",
          "sessions": [
            {
              "device": "Laptop",
              "ip": "10.0.0.2",
              "history": [
                {"login": "2025-08-01T10:00:00Z", "status": "success"},
                {"login": "2025-08-02T11:30:00Z", "status": "failed"}
              ]
            },
            {
              "device": "Mobile",
              "ip": "10.0.0.3",
              "history": []
            }
          ]
        }
      }
    },
    {
      "id": 2,
      "profile": {
        "name": "Bob",
        "contacts": [
          {"type": "email", "value": "bob@example.com"}
        ]
      },
      "settings": {
        "theme": "dark",
        "security": {
          "2FA": "false",
          "sessions": []
        }
      }
    }
  ],
  "logs": [
    {
      "level": "error",
      "message": "Database connection failed",
      "context": {
        "retryCount": 3,
        "lastTried": "2025-08-17T22:15:00Z",
        "errors": [
          {"code": "ECONNREFUSED", "at": {"host": "192.168.1.10", "port": 5432}},
          {"code": "ETIMEOUT", "at": {"host": "192.168.1.11", "port": 5432}}
        ]
      }
    },
    {
      "level": "info",
      "message": "System started",
      "context": {}
    }
  ],
  "extra": [
    "simple string",
    123,
    "true",
    "null",
    {"deepObject": {"level1": {"level2": {"level3": {"level4": {"level5": "END"}}}}}}
  ]
}


print(data["logs"]["level"])