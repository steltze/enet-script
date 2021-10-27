import yaml

user = 'nghielme'
with open(r'passwd.yml') as file:
    passwd = yaml.load(file, Loader=yaml.FullLoader)['passwd']
# generate combinations
import itertools

with open(r'explore.yml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

expl_config = config['explore']
expl_list = [v for k,v in expl_config.items()]
combinations = list(itertools.product(*expl_list))

with open('job.hcl') as f:
    lines = f.read()

for c in combinations:
    job = lines.format(reuse_factor=c[0], n_filters=c[1], clock_period=c[2], quantization=c[3], precision=c[4],
                       input_data=config['simulation']['input_data'],
                       output_predictions=config['simulation']['output_predictions'], user=user, passwd=passwd)
    f = open('jobs/job_rf{}_f{}_clk{}_q{}_{}.hcl'.format(c[0], c[1], c[2], c[3], c[4]), "w")
    f.write(job)
    f.close()