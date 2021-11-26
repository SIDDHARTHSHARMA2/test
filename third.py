import boto3

elb = boto3.client('elb')
loadbalancer = elb.create_load_balancer(
        LoadBalancerName='prajwal-hu-loadbalancer',
        Listeners=[
            {
                'Protocol': 'HTTP',
                'LoadBalancerPort': 80,
                'InstanceProtocol': 'HTTP',
                'InstancePort' : 80,
            },
        ],
        AvailabilityZones=[
            'us-east-2a','us-east-2b'
        ],
)

print("Elastic Load Balancer created: ")
print(loadbalancer)


#Add the instanceID to the loadbalancers
attach_inst = elb.register_instance_with_load_balancer(
        Instances=[
            {
                'InstanceId':'i-0bffe16b6f72c2637',
                'InstanceId':'i-053e5688bb385a989'
            },
        ]
)

print("Attaching Instances to loadbalancer")
print(attach_inst)
