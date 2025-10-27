from DIRAC.WorkloadManagementSystem.Agent.SiteDirector import SiteDirector

class GreenSiteDirector(SiteDirector):
    # override selectively; keep base logic intact
    def _getPilotOptions(self, queue: str) -> list[str]:
        opts = super()._getPilotOptions(queue)
        # add your custom flags/behavior here
        opts.append("--my-flag=1")
        return opts