class Membership:
    def bronze(self):
        access = 3
        membership_type = "Bronze"
        return membership_type, access 

    def silvar(self):
        access = 6
        membership_type = "Silver"
        return membership_type, access 
    
    def golden(self):    
        access = 12
        membership_type = "Golden"
        return membership_type, access 