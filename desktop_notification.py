from pynotifier import Notification

Notification(
    title="Jai Hind",
    description="welcome to python project, you have 15 unread Messages",
    duration=10,
    urgency=Notification).send()

