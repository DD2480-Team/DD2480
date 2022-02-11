from git import Repo
import shutil
# path to where this class will create the directory to pull the project into
gitDir = "./temp-git-dir/"

class GitRepo:
    """ Creates a repo object and checks out the given branch (remember the branch name is different if you have it locally)
        This will create it in your local filesystem currently at gitDir = "./temp-git-dir/"
    """
    def __init__(self, branchName) -> None:
        try:
            self.repo = Repo.clone_from("https://github.com/DD2480-Team/DD2480.git", gitDir, branch=branchName)
            print("Cloned repo from remote")
        except Exception as e:
            print("Git testing repo found at:", gitDir)
            if(str(e)[0:40] == "Cmd('git') failed due to: exit code(128)"):
                #you already have a directory called {gitDir="./temp-git-dir/"} so we'll use that one
                self.repo = Repo(gitDir)
            else:
                raise
        self.repoLocalPath = gitDir
        pullinfo = self.gitPull()
        print(pullinfo)
        #self.checkoutBranch("master")          #How to checkout a local branch  
        #self.checkoutBranch("origin/issue1")   #How to checkout a remote branch

        self.checkRepoNotBare()
        self.repo.config_reader()             # get a config reader for read-only access
        with self.repo.config_writer():       # get a config writer to change configuration
            pass                         # call release() to be sure changes are written and locks are released

    def checkRepoNotBare(self):
        """Checks to make sure the pulled repo isn't empty

        Returns:
            [bool]: False if repo is empty, True otherwise
        """
        if(self.repo.bare):
            print("Repo is bare :(")
            return False
        else:
            print("The repo contains stuff!")
            return True

    def forceClone(self, branchName):
        """Force a git clone (for example if you've deleted files, which git won't reset with a pull)

        Args:
            branchName (String): name of the branch you want to clone
        """
        try:
            shutil.rmtree(gitDir)
        except OSError as e:
            print("Error: %s : %s" % (gitDir, e.strerror))
        self.repo = Repo.clone_from("https://github.com/DD2480-Team/DD2480.git", gitDir, branch=branchName)
        print("Cloned repo from remote")

    def gitPull(self):
        """Perform a git pull, in repo and on branch ALREADY SPECIFIED

        Returns:
            [String]: stdout from the git pull
        """
        pullinfo = self.repo.git.pull()     #call git pull directly and read from stdout
        return pullinfo

    def gitStatus(self):
        """Perform a git status

        Returns:
            [String]: stdout from the git status
        """
        statusInfo = self.repo.git.status()     #call git pull directly and read from stdout
        return statusInfo

    def checkoutBranch(self, branchName):
        """ Check out the given branch from git 
            (won't change the git branch you're currently on in your terminal)

        Args:
            branchName (string): name as given when typing git branch -a
        """
        try:
            checkoutStatus = self.repo.git.checkout(branchName)
            print(checkoutStatus)
        except Exception as e:
            print(str(e))

if __name__=='__main__':
    gitrepo = GitRepo("master")

