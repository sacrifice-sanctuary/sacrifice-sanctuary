testsuite act_0:

    setup:
        $ print("Testing Act 0 (Prologue)")

        skip until "main_menu"
        click "Start"

    before testcase:
        $ print("New scene beginning...")

    after testcase:
        $ print("Scene completed.")

    teardown:
        $ print("Act 0 testing complete. Exiting...")
        exit

    testcase scene_1:
        description "Test Act 0 Scene 1"

        $ print("Skipping through Pandora dialogue...")
        advance until screen "pandora_room"

        $ print("Interacting with objects in room...")

        assert eval(roomtotal == 0)

        click id "pandora bed"
        advance until screen "pandora_room"
        assert eval(roomtotal == 1)

        click id "pandora wardrobe"
        advance until screen "pandora_room"
        assert eval(roomtotal == 2)

        click id "pandora bin"
        advance until screen "pandora_room"
        assert eval(roomtotal == 3)

        click id "pandora speaker"
        advance until screen "pandora_room"
        assert eval(roomtotal == 4)

        click id "pandora table"
        advance until screen "pandora_room"
        assert eval(roomtotal == 5)

        click id "pandora note"
        advance until screen "pandora_room"
        assert eval(roomtotal == 6)

        click id "pandora chair"
        advance until screen "pandora_room"
        assert eval(roomtotal == 7)

        click id "pandora door"
        advance until screen "pandora_room"
        assert eval(roomtotal == 8)

        click id "pandora clock"
        advance until screen "pandora_room"
        assert eval(roomtotal == 9)

        click id "pandora cactus"
        advance until screen "pandora_room"
        assert eval(roomtotal == 10)

        click id "pandora drawers"
        advance until screen "pandora_room"

        $ print("Skipping Darya cutscene...")

        advance until screen "pandora_room"

        assert eval(daryaroom == True)

        $ print("Leaving room...")

        click id "pandora door"
        click "Yes, let's have a look around outside"

        advance until screen "corrA1"

        pause 3.0
