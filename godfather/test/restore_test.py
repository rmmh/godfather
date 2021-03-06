import os
import pickle
import shutil

from .cli_test import *

class RestoreTest(CliTest):

  def test_restore(self):
    """Test that 'restore' restores a game file."""
    exec_godfather(["init", self.game_dir])
    exec_godfather(["run", "--setup_only", self.game_dir])

    # Create a backup file.
    backup_path = os.path.join(self.game_dir, "game.pickle.bac")
    shutil.copy(self.game_path, backup_path)
    moderator = pickle.load(open(backup_path, "rb"))
    moderator.fake_member = "Bananas"
    pickle.dump(moderator, open(backup_path, "wb"))

    # Restore the backup file.
    exec_godfather(["restore", self.game_dir, "--backup", backup_path])

    # Check that the backup file was restored.
    moderator = pickle.load(open(self.game_path, "rb"))
    self.assertEqual("Bananas", moderator.fake_member)
