import os
import glob
import shutil
import tarfile
import platform

from django.core.management.base import BaseCommand
from django.conf import settings

from lib.utils.io import get_url_content
from lib.utils import clogging
log = clogging.getColorLogger(__name__)


class Command(BaseCommand):
    help = "Setup go-vcf-tools"

    def handle(self, *args, **options):
        tmp_dir = os.path.join(settings.BASE_DIR, 'tmp')
        bin_dir = os.path.join(settings.BASE_DIR, 'bin')

        log.info('Fetching go-vcf-tools ...')
        url = '{repo}/releases/download/{tag}/{os_platform}.amd64.tar.gz'.format(repo='https://github.com/knmkr/go-vcf-tools',
                                                                                 tag='0.0.3',
                                                                                 os_platform=platform.system().lower())
        tar_gz = os.path.join(tmp_dir, 'go-vcf-tools.tar.gz')
        get_url_content(url, tar_gz, if_not_exists=True)

        log.info('Extracting go-vcf-tools ...')
        with tarfile.open(tar_gz, 'r') as tar:
            dst = os.path.join(tmp_dir, 'go-vcf-tools')
            tar.extractall(dst)
            for tool in glob.glob(os.path.join(tmp_dir, 'go-vcf-tools', '*', 'vcf-*')):
                shutil.copy(tool, bin_dir)

        os.remove(tar_gz)
        shutil.rmtree(dst)

        log.info('Fetching RsMergeArch ...')
        url = 'http://ftp.ncbi.nih.gov/snp/organisms/human_9606_b144_GRCh37p13/database/organism_data/RsMergeArch.bcp.gz'
        get_url_content(url, settings.RS_MERGE_ARCH_PATH, if_not_exists=True, md5='836289e6fe867bd5a6754802f05b2fb8')

        log.info('Done.')
