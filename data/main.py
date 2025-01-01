import os
import yaml
from dotenv import load_dotenv
from spotify_utils import SpotifyUtils
from user_utils import UserUtils
from kafka_utils import KafkaStreamer

load_dotenv()

# Environment Variables -> env file
SPOTIPY_CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")

KAFKA_BOOTSTRAP_SERVER = (
    os.environ.get("KAFKA_BROKER_ADDRESS") + ":" + os.environ.get("KAFKA_BROKER_PORT")
)

KAFKA_EVENTS_TOPIC = os.environ.get("KAFKA_EVENTS_TOPIC")

print(KAFKA_BOOTSTRAP_SERVER)
print(KAFKA_EVENTS_TOPIC)