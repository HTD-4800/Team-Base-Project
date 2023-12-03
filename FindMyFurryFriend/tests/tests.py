from channels.testing import WebsocketCommunicator
import json
import pytest
from FMFF.consumers import NotificationConsumer

@pytest.mark.asyncio
async def test_notification_consumer():
    # Create a WebSocket communicator for testing
    communicator = WebsocketCommunicator(NotificationConsumer.as_asgi())

    # Connect and check the connection was successful
    connected, _ = await communicator.connect()
    assert connected

    try:
        # Send a message to the consumer
        message_data = {'message': 'Test Message'}
        await communicator.send_json_to(message_data)

        # Receive and parse the response
        response = await communicator.receive_json_from()

        # Check that the response matches the expected message
        assert response == message_data
    finally:
        # Disconnect from the WebSocket
        await communicator.disconnect()
