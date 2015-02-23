#!/usr/bin/env python
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

def main():
    argument_spec = ec2_argument_spec()
    argument_spec.update(dict(

    )
    )

    module = AnsibleModule(
        argument_spec=argument_spec,
    )
    
	ec2_url, aws_access_key, aws_secret_key, region = get_ec2_creds(module)

	try:
	    iam = boto.iam.connection.IAMConnection(
	        aws_access_key_id=aws_access_key,
	        aws_secret_access_key=aws_secret_key,
	    )
	except boto.exception.NoAuthHandlerFound, e:
	    module.fail_json(msg=str(e))

from ansible.module_utils.basic import *
from ansible.module_utils.ec2 import *

main()