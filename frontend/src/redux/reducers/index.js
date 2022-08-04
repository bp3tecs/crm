import { combineReducers } from 'redux';
import Auth from './Auth';
import Theme from './Theme';
import Leads from './Leads';
import Users from './Users';
import Contacts from './Contacts';
import Companies from './Companies';
import profiles from './Profiles';
import Accounts from './Accounts';
const reducers = combineReducers({    
    auth: Auth,    
    theme: Theme,
    leads: Leads,
    users: Users,
    contacts: Contacts,
    companies: Companies,
    profiles: profiles,
    accounts:Accounts

});

export default reducers;
