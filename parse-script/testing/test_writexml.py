import unittest
import redis


def writeXml(redisEntry, pairs):
    if not pairs:
        return False
    try:
        redisEntry.ping()
    except AttributeError:
        return False
    
    for key, val in pairs.items():
        if key == 'subdomains':
            for subdomain in val:
                redisEntry.rpush('subdomains', subdomain)
        else:
            redisEntry.set(key, val)
    
    return [key for key in redisEntry.keys()]




class TestWriteXml(unittest.TestCase):

    def test_writeXml_no_pairs(self):
        redisEntry = redis.Redis(
                            host='localhost',
                            port=6000,
                            charset="utf-8",
                            decode_responses=True
                            )
        actual = writeXml(redisEntry, False)
        expected = False
        self.assertEqual(actual, expected)

    def test_writeXml_no_connection(self):
        pairTest = {'subdomains': ['http://secureline.tools.avast.com', 'http://gf.tools.avast.com', 'http://files.avast.com', 'https://files.avast.com', 'https://install.avcdn.net', 'http://bits.ff.avast.com', 'http://a381mp.avast.com', 'http://s.files.avast.com', 'http://bcu.tools.avast.com', 'http://iavs9x.u.avast.com', 'http://www.avg.com', 'https://www.avg.com', 'http://drup.d.avcdn.net', 'https://drup.d.avcdn.net', 'http://cleanup.u.avcdn.net', 'https://cleanup.u.avcdn.net', 'http://iabs.d.avast.com', 'http://avast.ustab.d.avcdn.net', 'http://files-download.avg.com', 'https://files-download.avg.com', 'http://download.ff.avast.com', 'http://tuneup.avast.tools.avcdn.net', 'http://cdn-download.avastbrowser.com', 'https://cdn-download.avastbrowser.com', 'http://mac-av.u.avcdn.net', 'https://mac-av.u.avcdn.net', 'http://iavs9x.avg.u.avcdn.net', 'http://beta9x.avg.u.avcdn.net', 'http://trackoff.d.avcdn.net', 'https://s-mac-sl.avcdn.net', 'https://s-bconprem.avcdn.net', 'https://bits.ff.avast.com', 'https://s-drup.avcdn.net', 'https://install-macsl.avcdn.net', 'https://s-install.avcdn.net', 'https://cdn-download.avgbrowser.com', 'https://s-trackoff.avcdn.net', 'https://bits.avcdn.net'], 'cookie:dlp-avast:amazon': 'mmm_amz_dlp_777_ppc_m', 'cookie:dlp-avast:baixaki': 'mmm_bxk_dlp_777_ppc_m', 'cookie:dlp-avast:computerbuild': 'mmm_cbd_dlp_777_ppc_m', 'cookie:dlp-avast:chip': 'mmm_cip_dlp_777_ppc_m', 'cookie:dlp-avast:comss': 'mmm_cms_dlp_777_ppc_m', 'cookie:dlp-avast:cnet': 'mmm_cnt_dlp_777_ppc_m', 'cookie:dlp-avast:dobreprogramy': 'mmm_dbp_dlp_777_ppc_m', 'cookie:dlp-avast:donwloaden': 'mmm_dld_dlp_777_ppc_m', 'cookie:dlp-avast:facebook': 'mmm_fcb_dlp_777_ppc_m', 'cookie:dlp-avast:filehippo': 'mmm_fhp_dlp_777_ppc_m', 'cookie:dlp-avast:forest': 'mmm_for_dlp_777_ppc_m', 'cookie:dlp-avast:html': 'mmm_htm_dlp_777_ppc_m', 'cookie:dlp-avast:homepate': 'mmm_htr_dlp_777_ppc_m', 'cookie:dlp-avast:naver': 'mmm_nav_dlp_777_ppc_m', 'cookie:dlp-avast:01net': 'mmm_net_dlp_777_ppc_m', 'cookie:dlp-avast:softpedia': 'mmm_sfp_dlp_777_ppc_m', 'cookie:dlp-avast:softonic': 'mmm_sft_dlp_777_ppc_m', 'cookie:dlp-avast:slunecnice': 'mmm_slc_dlp_777_ppc_m', 'cookie:dlp-avast:stahuj': 'mmm_sth_dlp_777_ppc_m', 'cookie:dlp-avast:tamindir': 'mmm_tam_dlp_777_ppc_m', 'cookie:dlp-avast:ultradownloads': 'mmm_uld_dlp_777_ppc_m', 'cookie:dlp-avast:uptodown': 'mmm_utd_dlp_777_ppc_m', 'cookie:dlp-avast:vector': 'mmm_vct_dlp_777_ppc_m', 'cookie:dlp-avg:amazon': 'mmm_amz_dlp_779_ppc_m', 'cookie:dlp-avg:baixaki': 'mmm_bxk_dlp_779_ppc_m', 'cookie:dlp-avg:computerbuild': 'mmm_cbd_dlp_779_ppc_m', 'cookie:dlp-avg:chip': 'mmm_cip_dlp_779_ppc_m', 'cookie:dlp-avg:comss': 'mmm_cms_dlp_779_ppc_m', 'cookie:dlp-avg:cnet': 'mmm_cnt_dlp_779_ppc_m', 'cookie:dlp-avg:dobreprogramy': 'mmm_dbp_dlp_779_ppc_m', 'cookie:dlp-avg:donwloaden': 'mmm_dld_dlp_779_ppc_m', 'cookie:dlp-avg:facebook': 'mmm_fcb_dlp_779_ppc_m', 'cookie:dlp-avg:filehippo': 'Mmm_fhp_dlp_779_ppc_m', 'cookie:dlp-avg:forest': 'mmm_for_dlp_779_ppc_m', 'cookie:dlp-avg:html': 'mmm_htm_dlp_779_ppc_m', 'cookie:dlp-avg:homepate': 'mmm_htr_dlp_779_ppc_m', 'cookie:dlp-avg:naver': 'mmm_nav_dlp_779_ppc_m', 'cookie:dlp-avg:01net': 'mmm_net_dlp_779_ppc_m', 'cookie:dlp-avg:softpedia': 'mmm_sfp_dlp_779_ppc_m', 'cookie:dlp-avg:softonic': 'mmm_sft_dlp_779_ppc_m', 'cookie:dlp-avg:slunecnice': 'mmm_slc_dlp_779_ppc_m', 'cookie:dlp-avg:stahuj': 'mmm_sth_dlp_779_ppc_m', 'cookie:dlp-avg:tamindir': 'mmm_tam_dlp_779_ppc_m', 'cookie:dlp-avg:ultradownloads': 'mmm_uld_dlp_779_ppc_m', 'cookie:dlp-avg:uptodown': 'mmm_utd_dlp_779_ppc_m', 'cookie:dlp-avg:vector': 'mmm_vct_dlp_779_ppc_m'}
        actual = writeXml(None, pairTest)
        expected = False
        self.assertEqual(actual, expected)
    
