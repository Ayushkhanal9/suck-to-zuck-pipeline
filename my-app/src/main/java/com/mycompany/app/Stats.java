package com.mycompany.app;

import com.fasterxml.jackson.annotation.JsonProperty;

public class Stats {
        @JsonProperty("Siera")
        private String siera;
        @JsonProperty("FB%")
        private String fb;
        @JsonProperty("xFIP")
        private String xFip;
        @JsonProperty("K/9")
        private String k9;
        @JsonProperty("GB%")
        private String gb;
        @JsonProperty("HR/FB")
        private String hrFB;

        public String getSiera() {
            return siera;
        }

        public String getFb() {
            return fb;
        }

        public String getxFip() {
            return xFip;
        }

        public String getK9() {
            return k9;
        }

        public String getGb() {
            return gb;
        }

        public String getHrFB() {
            return hrFB;
        }

        public void setSiera(String siera) {
            this.siera = siera;
        }

        public void setFb(String fb) {
            this.fb = fb;
        }

        public void setxFip(String xFip) {
            this.xFip = xFip;
        }

        public void setK9(String k9) {
            this.k9 = k9;
        }

        public void setGb(String gb) {
            this.gb = gb;
        }

        public void setHrFB(String hrFB) {
            this.hrFB = hrFB;
        }

}
