"""
Initial migration
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""create table RubberDuck (
        id      INTEGER
        primary key autoincrement,
        user_id BIGINT not null
    )""",
         "DROP TABLE RubberDuck")
]
